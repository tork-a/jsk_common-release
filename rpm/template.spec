Name:           ros-indigo-image-view2
Version:        2.0.16
Release:        1%{?dist}
Summary:        ROS image_view2 package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/image_view2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-image-geometry
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-image-view
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
BuildRequires:  numpy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-image-geometry
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-image-view
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  scipy

%description
A simple viewer for ROS image topics with draw-on features

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Sun Jun 19 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.16-1
- Autogenerated by Bloom

* Sun Jun 19 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.16-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.15-1
- Autogenerated by Bloom

* Mon Jun 13 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.15-0
- Autogenerated by Bloom

* Sat May 14 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.14-0
- Autogenerated by Bloom

* Fri Apr 29 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.13-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.12-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.11-0
- Autogenerated by Bloom

* Tue Dec 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.9-1
- Autogenerated by Bloom

* Tue Dec 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.9-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.8-0
- Autogenerated by Bloom

* Mon Dec 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.7-0
- Autogenerated by Bloom

* Thu Dec 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.6-0
- Autogenerated by Bloom

* Mon Nov 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Wed Nov 25 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.4-1
- Autogenerated by Bloom

* Fri Jul 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Tue Jul 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Sun Jun 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

* Mon May 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.71-0
- Autogenerated by Bloom

* Sat May 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.70-1
- Autogenerated by Bloom

* Sat May 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.70-0
- Autogenerated by Bloom

* Tue May 05 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.69-0
- Autogenerated by Bloom

* Tue May 05 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.68-0
- Autogenerated by Bloom

* Mon May 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.67-0
- Autogenerated by Bloom

* Fri Apr 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.66-0
- Autogenerated by Bloom

* Thu Apr 02 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.65-0
- Autogenerated by Bloom

* Wed Apr 01 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.64-0
- Autogenerated by Bloom

* Thu Feb 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.63-0
- Autogenerated by Bloom

* Tue Feb 17 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.62-0
- Autogenerated by Bloom

* Wed Feb 11 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.61-0
- Autogenerated by Bloom

* Wed Feb 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.60-1
- Autogenerated by Bloom

* Tue Feb 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.60-0
- Autogenerated by Bloom

* Tue Feb 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.59-1
- Autogenerated by Bloom

* Tue Feb 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.59-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.58-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.57-0
- Autogenerated by Bloom

* Wed Dec 17 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.56-0
- Autogenerated by Bloom

