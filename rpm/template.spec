Name:           ros-jade-jsk-data
Version:        2.0.13
Release:        0%{?dist}
Summary:        ROS jsk_data package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-depth-image-proc
Requires:       ros-jade-image-transport
Requires:       ros-jade-jsk-topic-tools
BuildRequires:  python-nose
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-roslint

%description
The jsk_data package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Apr 29 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.13-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.12-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.11-0
- Autogenerated by Bloom

* Tue Dec 15 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.9-1
- Autogenerated by Bloom

* Tue Dec 15 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.9-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.8-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.7-0
- Autogenerated by Bloom

* Thu Dec 03 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.6-0
- Autogenerated by Bloom

* Mon Nov 30 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Thu Nov 26 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.4-2
- Autogenerated by Bloom

* Sat Aug 01 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.3-1
- Autogenerated by Bloom

* Sat Aug 01 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Tue Jul 07 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Sun Jun 28 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Tue Jun 23 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 2.0.0-1
- Autogenerated by Bloom

