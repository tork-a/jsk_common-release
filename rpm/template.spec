Name:           ros-indigo-jsk-topic-tools
Version:        1.0.61
Release:        0%{?dist}
Summary:        ROS jsk_topic_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_topic_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-dynamic-tf-publisher
Requires:       ros-indigo-eigen-conversions
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roslaunch
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       ros-indigo-topic-tools
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-dynamic-tf-publisher
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp-tutorials
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-rosnode
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-rostopic
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-topic-tools

%description
jsk_topic_tools

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

* Wed Dec 10 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.55-1
- Autogenerated by Bloom

* Tue Dec 09 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.55-0
- Autogenerated by Bloom

* Sat Nov 15 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.54-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

