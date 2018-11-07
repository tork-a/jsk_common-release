Name:           ros-melodic-jsk-topic-tools
Version:        2.2.10
Release:        0%{?dist}
Summary:        ROS jsk_topic_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_topic_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       numpy
Requires:       opencv-python
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-dynamic-tf-publisher
Requires:       ros-melodic-eigen-conversions
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-image-transport
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-nodelet >= 1.9.11
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roslaunch
Requires:       ros-melodic-rosnode
Requires:       ros-melodic-rostime
Requires:       ros-melodic-rostopic
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-sound-play
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-tf
Requires:       ros-melodic-topic-tools
Requires:       scipy
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-dynamic-tf-publisher
BuildRequires:  ros-melodic-eigen-conversions
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-image-transport
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-nodelet >= 1.9.11
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roscpp-tutorials
BuildRequires:  ros-melodic-roslaunch
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-rosnode
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-rostime
BuildRequires:  ros-melodic-rostopic
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-topic-tools

%description
jsk_topic_tools

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Nov 07 2018 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.2.10-0
- Autogenerated by Bloom

* Thu Nov 01 2018 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.2.8-1
- Autogenerated by Bloom

