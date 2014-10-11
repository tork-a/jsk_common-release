Name:           ros-hydro-downward
Version:        1.0.48
Release:        0%{?dist}
Summary:        ROS downward package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/downward
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  glibc-devel(x86-32)
BuildRequires:  glibc-static
BuildRequires:  glibc-static(x86-32)
BuildRequires:  libstdc++-devel
BuildRequires:  libstdc++-devel(x86-32)
BuildRequires:  libstdc++-static
BuildRequires:  libstdc++-static(x86-32)
BuildRequires:  mercurial
BuildRequires:  python-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-rospack

%description
fast downward: PDDL Planner (http://www.fast-downward.org)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Oct 12 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

