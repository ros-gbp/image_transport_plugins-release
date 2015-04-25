Name:           ros-jade-theora-image-transport
Version:        1.9.2
Release:        0%{?dist}
Summary:        ROS theora_image_transport package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/image_transport_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       libogg-devel
Requires:       libtheora-devel
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-image-transport
Requires:       ros-jade-message-runtime
Requires:       ros-jade-pluginlib
Requires:       ros-jade-rosbag
Requires:       ros-jade-std-msgs
Requires:       ros-jade-tf
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-rosbag
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf

%description
Theora_image_transport provides a plugin to image_transport for transparently
sending an image stream encoded with the Theora codec.

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
* Sat Apr 25 2015 Julius Kammerl <jkammerl@willowgarage.com> - 1.9.2-0
- Autogenerated by Bloom

