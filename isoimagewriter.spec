%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
#define git 20230102

Summary:	Program to write hybrid ISO files onto USB disks
Name:		isoimagewriter
Version:	24.01.90
Release:	%{?git:0.%{git}.}1
License:	GPLv3+
Group:		File tools
Url:		https://invent.kde.org/utilities/isoimagewriter
%if 0%{?git:1}
# git clone https://invent.kde.org/utilities/isoimagewriter.git
# git archive --format=tar.gz -o ../isoimagewriter-0.8-$(date +%Y%m%d).tar.gz --prefix=isoimagewriter-master-%gitcommit/ master
Source0:	https://invent.kde.org/utilities/isoimagewriter/-/archive/%{name}-%{version}-%{git}.tar.gz
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	cmake(QGpgmeQt6)
BuildRequires:	pkgconfig(udev)

%description
ISO Image Writer is a tool to write a .iso file to a USB disk.

%prep
%autosetup -n %{name}-%{?git:master-%{gitcommit}}%{!?git:%{version}} -p1
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DUSE_KAUTH=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/isoimagewriter
%{_datadir}/applications/org.kde.isoimagewriter.desktop
%{_datadir}/icons/*/*/apps/org.kde.isoimagewriter.*
%{_datadir}/isoimagewriter
%{_datadir}/metainfo/org.kde.isoimagewriter.appdata.xml
