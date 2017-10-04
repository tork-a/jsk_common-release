Name:           ros-kinetic-jsk-tilt-laser
Version:        2.2.5
Release:        0%{?dist}
Summary:        ROS jsk_tilt_laser package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-laser-assembler
Requires:       ros-kinetic-laser-filters
Requires:       ros-kinetic-multisense-lib
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf-conversions
Requires:       ros-kinetic-urg-node
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-laser-assembler
BuildRequires:  ros-kinetic-laser-filters
BuildRequires:  ros-kinetic-multisense-lib
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf-conversions

%description
The jsk_tilt_laser package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Oct 04 2017 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.2.5-0
- Autogenerated by Bloom

* Thu Jan 12 2017 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.2.2-0
- Autogenerated by Bloom

* Sat Oct 22 2016 YoheiKakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 2.1.2-1
- Autogenerated by Bloom

