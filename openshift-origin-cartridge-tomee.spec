%global cartridgedir %{_libexecdir}/openshift/cartridges/v2/tomee

Summary:       Provides TOMEE support
Name:          openshift-origin-cartridge-tomee
Version:       0.6.27
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      lsof
Requires:      bc
Requires:      java-1.7.0-openjdk
Requires:      java-1.7.0-openjdk-devel
%if 0%{?rhel}
Requires:      maven3
%endif
%if 0%{?fedora}
Requires:      maven
%endif
BuildRequires: jpackage-utils
BuildArch:     noarch

%description
Provides TomeEE support to OpenShift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post
# To modify an alternative you should:
# - remove the previous version if it's no longer valid
# - install the new version with an increased priority
# - set the new version as the default to be safe

%if 0%{?rhel}
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/java/apache-maven-3.0.3 100
alternatives --set maven-3.0 /usr/share/java/apache-maven-3.0.3
%endif

%if 0%{?fedora}
alternatives --remove maven-3.0 /usr/share/java/apache-maven-3.0.3
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/maven 102
alternatives --set maven-3.0 /usr/share/maven
%endif

%{_sbindir}/oo-admin-cartridge --action install --source %{cartridgedir}


%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Thu Oct 31 2013 Filirom1 <Filirom1@gmail.com> 0.6.27-1
- clean work and conf/<ENGINE NAME> (Filirom1@gmail.com)
- Add OpenEJB javaagent (Filirom1@gmail.com)
- fix tab (filirom1@gmail.com)
- doc remove restart tomcat after git push, it's already done
  (filirom1@gmail.com)

* Tue Oct 29 2013 Filirom1 <Filirom1@gmail.com> 0.6.26-1
- add cluster (Filirom1@gmail.com)

* Mon Oct 21 2013 Filirom1 <Filirom1@gmail.com> 0.6.25-1
- Make it works with openshift online

* Mon Oct 21 2013 Filirom1 <Filirom1@gmail.com>
- make it works on OpenShift Online

* Thu Jul 04 2013 Filirom1 <Filirom1@gmail.com> 0.6.23-1
- Merge branch 'master' of https://github.com/AtosWorldline/openshift-
  cartridge-tomee (Filirom1@gmail.com)
- update ROOT.war (Filirom1@gmail.com)
- update readme (loic.rodier@atos.net)
- update README for TomEE 1.6 (Filirom1@gmail.com)

* Wed Jul 03 2013 Filirom1 <Filirom1@gmail.com> 0.6.22-1
- add tomee6 (Filirom1@gmail.com)
- unpack wars (Filirom1@gmail.com)

* Wed Jul 03 2013 Filirom1 <Filirom1@gmail.com>
- add tomee6 (Filirom1@gmail.com)
- unpack wars (Filirom1@gmail.com)

* Wed Jul 03 2013 Filirom1 <Filirom1@gmail.com>
- add tomee6 (Filirom1@gmail.com)
- unpack wars (Filirom1@gmail.com)

* Mon Jul 01 2013 Filirom1 <Filirom1@gmail.com> 0.6.19-1
- TomEE 1.5.1 is more stable than 1.5.2 (Filirom1@gmail.com)
- s/Filirom1/AtosWorldline/g (Filirom1@gmail.com)

* Mon Jul 01 2013 Filirom1 <Filirom1@gmail.com> 0.6.18-1
- update install script (Filirom1@gmail.com)

* Mon Jul 01 2013 Filirom1 <Filirom1@gmail.com> 0.6.17-1
- add maker skip_maven_build (Filirom1@gmail.com)

* Mon Jul 01 2013 Filirom1 <Filirom1@gmail.com> 0.6.16-1
- do not talk about maven build (Filirom1@gmail.com)
- update README (Filirom1@gmail.com)

* Tue Jun 25 2013 Filirom1 <Filirom1@gmail.com> 0.6.15-1
- s/OPENSHIFT_TOMCAT/OPENSHIFT_TOMEE/g (Filirom1@gmail.com)
- Automatic commit of package [openshift-origin-cartridge-tomee] release
  [0.6.11-1]. (Filirom1@gmail.com)
- fix metadata files (Filirom1@gmail.com)
- update the README (Filirom1@gmail.com)
- Automatic commit of package [openshift-origin-cartridge-tomee] release
  [0.6.7-1]. (Filirom1@gmail.com)
- update tomee configuration file (Filirom1@gmail.com)
- chmod +x (Filirom1@gmail.com)

* Tue Jun 25 2013 Filirom1 <Filirom1@gmail.com> 0.6.14-1
- rename TOMCAT in TOMEE (Filirom1@gmail.com)

* Tue Jun 25 2013 Filirom1 <Filirom1@gmail.com> 0.6.13-1
- s/SYSTEM_TOMCAT/SYSTEM_TOMEE/g (Filirom1@gmail.com)

* Tue Jun 25 2013 Filirom1 <Filirom1@gmail.com> 0.6.12-1
- s/OPENSHIFT_TOMCAT/OPENSHIFT_TOMEE/g (Filirom1@gmail.com)

* Tue Jun 25 2013 Filirom1 <Filirom1@gmail.com> 0.6.11-1
- fix cartridge vendor (Filirom1@gmail.com)

* Tue Jun 25 2013 Filirom1 <Filirom1@gmail.com> 0.6.10-1
- fix manifest.yml (Filirom1@gmail.com)

* Tue Jun 25 2013 Filirom1 <Filirom1@gmail.com> 0.6.9-1
- fix vendor_name does not match pattern /\A[a-z][a-z0-9_]*\z/.: 'Cartridge-
  Vendor' (Filirom1@gmail.com)

* Tue Jun 25 2013 Filirom1 <Filirom1@gmail.com> 0.6.8-1
- fix spec file (Filirom1@gmail.com)
- update the README (Filirom1@gmail.com)

* Tue Jun 25 2013 Filirom1 <Filirom1@gmail.com> 0.6.7-1
- new package built with tito

* Fri Jun 21 2013 Filirom1 <Filirom1@gmail.com> 0.6.6-1
- fix vendor_name (Filirom1@gmail.com)

* Fri Jun 21 2013 Filirom1 <Filirom1@gmail.com> 0.6.5-1
- s/filirom1/AtosWorldline/g (filirom1@gmail.com)
- restart is not mandatory (filirom1@gmail.com)
- Automatic commit of package [openshift-origin-cartridge-tomcat] release
  [0.6.4-1]. (filirom1@gmail.com)
- fix tomcat 6.0 server.xml (filirom1@gmail.com)
- explain how to buil an RPM (filirom1@gmail.com)
- Automatic commit of package [openshift-origin-cartridge-tomcat] release
  [0.6.3-1]. (filirom1@gmail.com)
- forget one jboss (filirom1@gmail.com)
- looks better with 6.0 (filirom1@gmail.com)
- Automatic commit of package [openshift-origin-cartridge-tomcat] release
  [0.6.2-1]. (filirom1@gmail.com)
- dos2unix (filirom1@gmail.com)
- Automatic commit of package [openshift-origin-cartridge-tomcat] release
  [0.6.1-1]. (filirom1@gmail.com)
- Initialized to use tito. (filirom1@gmail.com)
- fix JDK path (filirom1@gmail.com)
- update SYSTEM_TOMEE_DIR (filirom1@gmail.com)
- dos2unix (filirom1@gmail.com)
- chmod +x (filirom1@gmail.com)
- 'redhat' is reserved.: 'Cartridge-Vendor' (filirom1@gmail.com)
- replace jboss ews reference by tomcat (filirom1@gmail.com)
- fork jbossews (filirom1@gmail.com)

* Fri Jun 21 2013 Filirom1 <Filirom1@gmail.com> 0.6.4-1
- fix tomcat 6.0 server.xml (Filirom1@gmail.com)
- explain how to buil an RPM (Filirom1@gmail.com)

* Fri Jun 21 2013 Filirom1 <Filirom1@gmail.com> 0.6.3-1
- forget one jboss (Filirom1@gmail.com)
- looks better with 6.0 (Filirom1@gmail.com)

* Fri Jun 21 2013 Filirom1 <Filirom1@gmail.com> 0.6.2-1
- new package built with tito

* Fri Jun 21 2013 Filirom1 <Filirom1@gmail.com> 0.6.1-1
- new package built with tito

* Thu Jun 20 2013 Filirom1 <filirom1@gmail.com> 0.6.1-1
- Fork jbossews to provide tomcat instead (filirom1@gmail.com)

* Tue Jun 18 2013 Adam Miller <admiller@redhat.com> 0.5.3-1
- Merge pull request #2881 from ironcladlou/bz/972979
  (dmcphers+openshiftbot@redhat.com)
- Bug 972979: Don't include ROOT.war in initial Git repository
  (ironcladlou@gmail.com)

* Mon Jun 17 2013 Adam Miller <admiller@redhat.com> 0.5.2-1
- Bug 974923: Fix inaccurate Cart-Data env var references
  (ironcladlou@gmail.com)
- First pass at removing v1 cartridges (dmcphers@redhat.com)
- Bug 973825 (dmcphers@redhat.com)
- add APP_UUID to process (bdecoste@gmail.com)
- Use -z with quotes (dmcphers@redhat.com)
- WIP Cartridge Refactor - Fix setups to be reentrant (jhonce@redhat.com)
- Make Install-Build-Required default to false (ironcladlou@gmail.com)

* Thu May 30 2013 Adam Miller <admiller@redhat.com> 0.5.1-1
- bump_minor_versions for sprint 29 (admiller@redhat.com)

* Wed May 29 2013 Adam Miller <admiller@redhat.com> 0.4.6-1
- Bug 965591 (dmcphers@redhat.com)

* Thu May 23 2013 Adam Miller <admiller@redhat.com> 0.4.5-1
- Merge pull request #2605 from ironcladlou/dev/v2carts/jbossews
  (dmcphers+openshiftbot@redhat.com)
- Support OPENSHIFT_INTERNAL_* variables in jbossews v2 (ironcladlou@gmail.com)
- Bug 966255: Remove OPENSHIFT_INTERNAL_* references from v2 carts
  (ironcladlou@gmail.com)

* Wed May 22 2013 Adam Miller <admiller@redhat.com> 0.4.4-1
- Bug 962662 (dmcphers@redhat.com)
- Merge pull request #2560 from bdecoste/master
  (dmcphers+openshiftbot@redhat.com)
- add generic-java hook (bdecoste@gmail.com)
- Merge pull request #2554 from pmorie/bugs/964348
  (dmcphers+openshiftbot@redhat.com)
- Fix bug 964348 (pmorie@gmail.com)
- Merge pull request #2550 from ironcladlou/bz/965012
  (dmcphers+openshiftbot@redhat.com)
- Bug 965012: Generate initial ROOT.war dynamically on install for jboss
  cartridges (ironcladlou@gmail.com)

* Mon May 20 2013 Dan McPherson <dmcphers@redhat.com> 0.4.3-1
- Bug 964093: Generate OPENSHIFT_JBOSSEWS_VERSION during jbossews install
  (ironcladlou@gmail.com)
- spec file cleanup (tdawson@redhat.com)

* Thu May 16 2013 Adam Miller <admiller@redhat.com> 0.4.2-1
- Bug 962324: Fix jbossews stop logic to tolerate missing pidfile
  (ironcladlou@gmail.com)
- process-version -> update-configuration (dmcphers@redhat.com)
- Bug 963156 (dmcphers@redhat.com)
- <cartridge-jbossews> Bug 961628 - Fix Categories listed (jdetiber@redhat.com)
- WIP Cartridge Refactor -- Cleanup spec files (jhonce@redhat.com)
- Minor compatibility fixes for jbossews (ironcladlou@gmail.com)

* Wed May 08 2013 Adam Miller <admiller@redhat.com> 0.4.1-1
- bump_minor_versions for sprint 28 (admiller@redhat.com)

* Wed May 08 2013 Adam Miller <admiller@redhat.com> 0.3.8-1
- Bug 960650: Integrate with mysql and postgresql cartridges by default
  (ironcladlou@gmail.com)

* Tue May 07 2013 Adam Miller <admiller@redhat.com> 0.3.7-1
- Merge pull request #2353 from detiber/bz959844
  (dmcphers+openshiftbot@redhat.com)
- Bug 959844 - JBoss EWS v2 Cartridge fixes for EWS1.0 (jdetiber@redhat.com)

* Mon May 06 2013 Adam Miller <admiller@redhat.com> 0.3.6-1
- Bug 959132: Add cron cartridge integration (ironcladlou@gmail.com)

* Fri May 03 2013 Adam Miller <admiller@redhat.com> 0.3.5-1
- Special file processing (fotios@redhat.com)
- Validate cartridge and vendor names under certain conditions
  (asari.ruby@gmail.com)

* Thu May 02 2013 Adam Miller <admiller@redhat.com> 0.3.4-1
- Bug 958617 - Add missing env var (jhonce@redhat.com)

* Tue Apr 30 2013 Adam Miller <admiller@redhat.com> 0.3.3-1
- Merge pull request #2280 from mrunalp/dev/auto_env_vars
  (dmcphers+openshiftbot@redhat.com)
- Env var WIP. (mrunalp@gmail.com)
- Merge pull request #2275 from jwhonce/wip/cartridge_path
  (dmcphers+openshiftbot@redhat.com)
- Merge pull request #2270 from ironcladlou/dev/v2carts/jbossews
  (dmcphers+openshiftbot@redhat.com)
- Merge pull request #2201 from BanzaiMan/dev/hasari/c276
  (dmcphers+openshiftbot@redhat.com)
- Card online_runtime_266 - Renamed OPENSHIFT_<short name>_PATH to
  OPENSHIFT_<short name>_PATH_ELEMENT (jhonce@redhat.com)
- Implement multi-versioned jbossews-1.0/2.0 v2 cartridge
  (ironcladlou@gmail.com)
- Card 276 (asari.ruby@gmail.com)

* Mon Apr 29 2013 Adam Miller <admiller@redhat.com> 0.3.2-1
- Add health urls to each v2 cartridge. (rmillner@redhat.com)
- Merge pull request #2252 from danmcp/master
  (dmcphers+openshiftbot@redhat.com)
- Bug 952606: Fix JAVA_HOME/PATH switching with java7 marker
  (ironcladlou@gmail.com)
- Bug 957073 (dmcphers@redhat.com)

* Thu Apr 25 2013 Adam Miller <admiller@redhat.com> 0.3.1-1
- Bug 956626: Fix jbossews-2.0 paths (ironcladlou@gmail.com)
- Card online_runtime_266 - Build PATH from
  CARTRIDGE_<CARTRIDGE_SHORT_NAME>_PATH (jhonce@redhat.com)
- Split v2 configure into configure/post-configure (ironcladlou@gmail.com)
- more install/post-install scripts (dmcphers@redhat.com)
- Implement hot deployment for V2 cartridges (ironcladlou@gmail.com)
- Update outdated links in 'cartridges' directory. (asari.ruby@gmail.com)
- Adding V2 Format to all v2 cartridges (calfonso@redhat.com)
- Bug 928675 (asari.ruby@gmail.com)
- V2 documentation refactoring (ironcladlou@gmail.com)
- V2 cartridge documentation updates (ironcladlou@gmail.com)
- bump_minor_versions for sprint 2.0.26 (tdawson@redhat.com)

* Tue Apr 16 2013 Troy Dawson <tdawson@redhat.com> 0.2.7-1
- Setting mongodb connection hooks to use the generic nosqldb name
  (calfonso@redhat.com)

* Mon Apr 15 2013 Adam Miller <admiller@redhat.com> 0.2.6-1
- V2 action hook cleanup (ironcladlou@gmail.com)
- Merge pull request #2065 from jwhonce/wip/manifest_scrub
  (dmcphers+openshiftbot@redhat.com)
- cleanup (dmcphers@redhat.com)
- Merge pull request #2053 from calfonso/master
  (dmcphers+openshiftbot@redhat.com)
- WIP Cartridge Refactor - Scrub manifests (jhonce@redhat.com)
- Merge pull request #2052 from ironcladlou/dev/v2carts/jbossews-threaddump
  (dmcphers@redhat.com)
- Adding connection hook for mongodb There are three leading params we don't
  care about, so the hooks are using shift to discard. (calfonso@redhat.com)
- Add threaddump declaration to jbossews manifest (ironcladlou@gmail.com)
- Documentation for action hooks (ironcladlou@gmail.com)

* Fri Apr 12 2013 Adam Miller <admiller@redhat.com> 0.2.5-1
- SELinux, ApplicationContainer and UnixUser model changes to support oo-admin-
  ctl-gears operating on v1 and v2 cartridges. (rmillner@redhat.com)

* Wed Apr 10 2013 Adam Miller <admiller@redhat.com> 0.2.4-1
- Merge pull request #1974 from brenton/v2_post2 (dmcphers@redhat.com)
- Merge pull request #1967 from ironcladlou/dev/v2carts/jbossews
  (dmcphers@redhat.com)
- Registering/installing the cartridges in the rpm %%post (bleanhar@redhat.com)
- Update template app and cart documentation (ironcladlou@gmail.com)

* Tue Apr 09 2013 Adam Miller <admiller@redhat.com> 0.2.3-1
- Merge pull request #1962 from danmcp/master (dmcphers@redhat.com)
- Merge pull request #1950 from mrunalp/dev/remotedeploy (dmcphers@redhat.com)
- jenkins WIP (dmcphers@redhat.com)
- Rename cideploy to geardeploy. (mrunalp@gmail.com)
- Bug 949510: Fix reversed Java 7 marker detection (ironcladlou@gmail.com)
- Merge pull request #1942 from ironcladlou/dev/v2carts/vendor-changes
  (dmcphers+openshiftbot@redhat.com)
- Remove vendor name from installed V2 cartridge path (ironcladlou@gmail.com)

* Mon Apr 08 2013 Adam Miller <admiller@redhat.com> 0.2.2-1
- Merge pull request #1930 from mrunalp/dev/cart_hooks (dmcphers@redhat.com)
- Add hooks for other carts. (mrunalp@gmail.com)
- Fix Jenkins deploy cycle (ironcladlou@gmail.com)
- Refactor v2 cartridge SDK location and accessibility (ironcladlou@gmail.com)
- Minor EWS spec fix to avoid gcj issues (bleanhar@redhat.com)
- adding all the jenkins jobs (dmcphers@redhat.com)
- Adding jenkins templates to carts (dmcphers@redhat.com)

* Thu Mar 28 2013 Adam Miller <admiller@redhat.com> 0.2.1-1
- bump_minor_versions for sprint 26 (admiller@redhat.com)

* Wed Mar 27 2013 Adam Miller <admiller@redhat.com> 0.1.3-1
- Bug 927570: Fix jbossews threaddump control action (ironcladlou@gmail.com)

* Thu Mar 21 2013 Adam Miller <admiller@redhat.com> 0.1.2-1
- Fix jbossews v2 cartridge and implement build (ironcladlou@gmail.com)

* Tue Mar 19 2013 Dan McPherson <dmcphers@redhat.com> 0.1.1-1
- new package built with tito

* Tue Mar 19 2013 Dan Mace <ironcladlou@gmail.com> 0.1.0-1
- new package built with tito

