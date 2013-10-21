# OpenShift TomEE Community Cartridge

The `tomee` cartridge provides TomEE on OpenShift via a manual tomee install.

This cartridge has special functionality to enable integration with OpenShift and with other
cartridges. See the [Cartridge Integrations](#cartridge-integrations) and
[Environment Variable Replacement Support](#environment-variable-replacement-support) sections
for details.

## Template Repository Layout

    webapps/           Location for built WARs (details below)
    .openshift/        Location for OpenShift specific files
      config/          Location for configuration files such as server.xml, tomee.xml
      action_hooks/    See the Action Hooks documentation [1]
      markers/         See the Markers section [2]

\[1\] [Action Hooks documentation](https://github.com/openshift/origin-server/blob/master/node/README.writing_applications.md#action-hooks)
\[2\] [Markers](#markers)

Note: Every time you push, everything in your remote repo directory is recreated.
      Please store long term items (like an sqlite database) in the OpenShift
      data directory, which will persist between pushes of your repo.
      The OpenShift data directory is accessible via an environment variable `OPENSHIFT_DATA_DIR`.

## Layout and deployment option details

Contrary to the [tomcat community cartridge](https://github.com/AtosWorldline/openshift-cartridge-tomcat-community), the prefered way to deploy your application is to put your wars in the webapps directory.

1) You can commit pre-built wars into `webapps`.

Basic workflows for deploying pre-built content (each operation will require associated
Git add/commit/push operations to take effect):

1. Add new zipped content and deploy it:
  * `cp target/example.war webapps/`
2. Undeploy currently deployed content:
  * `git rm webapps/example.war`
3. Replace currently deployed zipped content with a new version and deploy it:
  * `cp target/example.war webapps/`

Note: You can get the information in the uri above from running `rhc domain show`

Note 2: To deploy at /, name your war ROOT.war

If you have already committed large files to your Git repo, you rewrite or reset the history of those files in Git
to an earlier point in time and then `git push --force` to apply those changes on the remote OpenShift server.  A 
`git gc` on the remote OpenShift repo can be forced with (Note: tidy also does other cleanup including clearing log
files and tmp dirs):

`rhc app tidy -a appname`

The `webapps` directory is the location end users can place 
their deployment content (e.g. war, ear, jar, sar files) to have it 
automatically deployed into the server runtime.

## Environment Variables

The Tomcat cartridge provides several environment variables to reference for ease
of use:

    OPENSHIFT_TOMEE_IP          The IP address used to bind TOMEE
    OPENSHIFT_TOMEE_HTTP_PORT   The TOMEE listening port
    OPENSHIFT_TOMEE_JPDA_PORT   The TOMEE JPDA listening port

For more information about environment variables, consult the
[OpenShift Application Author Guide](https://github.com/openshift/origin-server/blob/master/node/README.writing_applications.md).

### Environment Variable Replacement Support

The `tomee` cart provides special environment variable replacement functionality for some of the Tomcat configuration files.
For the following configuration files:

  * `.openshift/config/server.xml`
  * `.openshift/config/context.xml`

Ant-style environment replacements are supported for all `OPENSHIFT_`-prefixed environment variables in the application. For
example, the following replacements are valid in `server.xml`:

      <Connector address="${OPENSHIFT_TOMEE_IP}"
                 port="${OPENSHIFT_TOMEE_HTTP_PORT}"
                 protocol="HTTP/1.1"
                 connectionTimeout="20000"
                 redirectPort="8443" />

During server startup, the configuration files in the source repository are processed to replace `OPENSHIFT_*` values, and the
resulting processed file is copied to the live Tomcat configuration directory.


## Cartridge Integrations

The `tomee` cart has out-of-the-box integration support with the RedHat `postgresql` and `mysql` cartridges. The default
`tomee.xml` contains two basic JDBC `Resource` definitions, `jdbc/MysqlDS` and `jdbc/PostgreSQLDS`, which will be automatically
configured to work with their respective cartridges if installed into your application.


## Markers

Adding marker files to `.openshift/markers` will have the following effects:

    enable_jpda          Will enable the JPDA socket based transport on the java virtual
                         machine running the Tomcat server. This enables
                         you to remotely debug code running inside Tomcat.
    
    java7                Will run Tomcat with Java7 if present. If no marker is present
                         then the baseline Java version will be used (currently Java6)

## Install system dependecies
 
    $ yum install bc java-1.6.0-openjdk-devel java-1.7.0-openjdk-devel

## Download TomEE 1.5 and TomEE 1.6 and install them in `/opt/apache-tomee-X.Y`

    $ cd /opt
    $ wget http://repo1.maven.org/maven2/org/apache/openejb/apache-tomee/1.5.1/apache-tomee-1.5.1-jaxrs.tar.gz
    $ tar xvzf apache-tomee-1.5.1-jaxrs.tar.gz
    $ ln -s /opt/apache-tomee-jaxrs-1.5.1 /opt/apache-tomee-1.5
    $ wget https://repository.apache.org/content/groups/snapshots/org/apache/openejb/apache-tomee/1.6.0-SNAPSHOT/apache-tomee-1.6.0-20130703.041224-115-jaxrs.tar.gz
    $ tar xvzf apache-tomee-1.6.0-20130703.041224-115-jaxrs.tar.gz
    $ ln -s /opt/apache-tomee-jaxrs-1.6.0-SNAPSHOT apache-tomee-1.6

## Test as a download cartridge

Make sure this option is enable the the broker config.

    DOWNLOAD_CARTRIDGES_ENABLED="true"

Then create a cartridge with this URL: <http://cartreflect-claytondev.rhcloud.com/reflect?github=AtosWorldline/openshift-cartridge-tomee>

## Install as a RPM

Build the RPM.

    $ yum install tito
    $ tito init # only the first time you use tito for this cartridge
    $ tito tag
    $ tito build --rpm --test
    ...
    Successfully built: /tmp/tito/openshift-origin-cartridge-tomee-0.6.7-1.git.0.3ad7ce3.el6.src.rpm /tmp/tito/noarch/openshift-origin-cartridge-tomee-0.6.7-1.git.0.3ad7ce3.el6.noarch.rpm

On the node

    $ yum install /tmp/tito/noarch/openshift-origin-cartridge-tomee-0.6.7-1.git.0.3ad7ce3.el6.noarch.rpm

On the broker

    $ oo-admin-broker-cache --clear --console
