Name:           ros-hydro-jsk-common
Version:        1.0.60
Release:        0%{?dist}
Summary:        ROS jsk_common package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-assimp-devel
Requires:       ros-hydro-bayesian-belief-networks
Requires:       ros-hydro-downward
Requires:       ros-hydro-dynamic-tf-publisher
Requires:       ros-hydro-ff
Requires:       ros-hydro-ffha
Requires:       ros-hydro-image-view2
Requires:       ros-hydro-jsk-footstep-msgs
Requires:       ros-hydro-jsk-gui-msgs
Requires:       ros-hydro-jsk-hark-msgs
Requires:       ros-hydro-jsk-network-tools
Requires:       ros-hydro-jsk-tilt-laser
Requires:       ros-hydro-jsk-tools
Requires:       ros-hydro-jsk-topic-tools
Requires:       ros-hydro-libsiftfast
Requires:       ros-hydro-mini-maxwell
Requires:       ros-hydro-multi-map-server
Requires:       ros-hydro-nlopt
Requires:       ros-hydro-opt-camera
Requires:       ros-hydro-posedetection-msgs
Requires:       ros-hydro-rospatlite
Requires:       ros-hydro-rosping
Requires:       ros-hydro-rostwitter
Requires:       ros-hydro-sklearn
Requires:       ros-hydro-speech-recognition-msgs
Requires:       ros-hydro-virtual-force-publisher
Requires:       ros-hydro-voice-text
BuildRequires:  ros-hydro-catkin

%description
Metapackage that contains commonly used toolset for jsk-ros-pkg

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
* Tue Feb 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.60-0
- Autogenerated by Bloom

* Tue Feb 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.59-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.58-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.57-0
- Autogenerated by Bloom

* Sun Dec 21 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.56-0
- Autogenerated by Bloom

* Tue Dec 09 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.55-0
- Autogenerated by Bloom

* Sat Nov 15 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.54-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Mon Oct 20 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.51-0
- Autogenerated by Bloom

* Tue Oct 14 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.49-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

