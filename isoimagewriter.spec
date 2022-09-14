%define git 20220905
%define gitcommit 12bcf4045a52eab5c48a672e37722065633af0f6

Summary:	Program to write hybrid ISO files onto USB disks
Name:		isoimagewriter
Version:	0.8
Release:	0.%{git}.1
License:	GPLv3+
Group:		File tools
Url:		https://invent.kde.org/utilities/isoimagewriter
# git clone https://invent.kde.org/utilities/isoimagewriter.git
# git archive --format=tar.gz -o ../isoimagewriter-0.8-$(date +%Y%m%d).tar.gz --prefix=isoimagewriter-master-%gitcommit/ master
Source0:	https://invent.kde.org/utilities/isoimagewriter/-/archive/%{name}-%{version}-%{git}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	pkgconfig(udev)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
Requires:	kauth

%description
ISO Image Writer is a tool to write a .iso file to a USB disk.

%prep
%autosetup -n %{name}-%{git} -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_kde5_libexecdir}/kauth/%{name}_helper
%{_datadir}/applications/org.kde.isoimagewriter.desktop
%{_datadir}/dbus-1/system-services/org.kde.isoimagewriter.service
%{_datadir}/dbus-1/system.d/org.kde.isoimagewriter.conf
%{_datadir}/%{name}/*.gpg
%{_datadir}/metainfo/org.kde.isoimagewriter.appdata.xml
%{_datadir}/polkit-1/actions/org.kde.isoimagewriter.policy
