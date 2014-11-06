Name:           ros-indigo-jsk-tilt-laser
Version:        1.0.53
Release:        0%{?dist}
Summary:        ROS jsk_tilt_laser package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-dynamixel-controllers
Requires:       ros-indigo-laser-assembler
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf-conversions
Requires:       ros-indigo-urg-node
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-laser-assembler
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-tf-conversions

%description
The jsk_tilt_laser package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Nov 06 2014 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Sun Oct 12 2014 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

