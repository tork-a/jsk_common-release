Name:           ros-indigo-jsk-footstep-msgs
Version:        1.0.65
Release:        0%{?dist}
Summary:        ROS jsk_footstep_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_footstep_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation

%description
jsk_footstep_msgs

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

