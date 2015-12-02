Name:           ros-indigo-jsk-tools
Version:        2.0.6
Release:        0%{?dist}
Summary:        ROS jsk_tools package

Group:          Development/Libraries
License:        Apache License 2.0
URL:            http://ros.org/wiki/jsk_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-axis-camera
Requires:       ros-indigo-jsk-network-tools
Requires:       ros-indigo-jsk-topic-tools
Requires:       ros-indigo-pr2-computer-monitor
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-rosemacs
Requires:       ros-indigo-rosgraph-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-reconfigure
BuildRequires:  git
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rosgraph-msgs

%description
Includes emacs scripts, ros tool alias generator, and launch doc generator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 03 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.6-0
- Autogenerated by Bloom

* Mon Nov 30 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Wed Nov 25 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.4-1
- Autogenerated by Bloom

* Fri Jul 24 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Tue Jul 07 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Sun Jun 28 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

* Mon May 18 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.71-0
- Autogenerated by Bloom

* Sat May 09 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.70-1
- Autogenerated by Bloom

* Sat May 09 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.70-0
- Autogenerated by Bloom

* Tue May 05 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.69-0
- Autogenerated by Bloom

* Tue May 05 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.68-0
- Autogenerated by Bloom

* Mon May 04 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.67-0
- Autogenerated by Bloom

* Fri Apr 03 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.66-0
- Autogenerated by Bloom

* Thu Apr 02 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.65-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.64-0
- Autogenerated by Bloom

* Thu Feb 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.63-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.62-0
- Autogenerated by Bloom

* Wed Feb 11 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.61-0
- Autogenerated by Bloom

* Wed Feb 04 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.60-1
- Autogenerated by Bloom

* Tue Feb 03 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.60-0
- Autogenerated by Bloom

* Tue Feb 03 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.59-1
- Autogenerated by Bloom

* Tue Feb 03 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.59-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.58-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.57-0
- Autogenerated by Bloom

* Wed Dec 17 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.56-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.55-1
- Autogenerated by Bloom

* Tue Dec 09 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.55-0
- Autogenerated by Bloom

* Sat Nov 15 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.54-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

