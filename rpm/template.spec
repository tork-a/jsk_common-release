%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-virtual-force-publisher
Version:        2.2.11
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS virtual_force_publisher package

License:        BSD
URL:            http://ros.org/wiki/virtual_force_publisher
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-kdl-parser
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-tf-conversions
Requires:       ros-noetic-urdf
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-kdl-parser
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-tf-conversions
BuildRequires:  ros-noetic-urdf
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
publish end effector's force, which is estmated from joint torque value

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Sat Jul 11 2020 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.2.11-2
- Autogenerated by Bloom

