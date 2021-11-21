%global debug_package %{nil}

Name:	    pinta
Version:	1.7.1
Release:	1
Summary:	An easy to use drawing and image editing program
Group:		Graphics

# the code is licensed under the MIT license while the icons are licensed as CC-BY
License:	MIT and CC-BY
URL:		http://pinta-project.com/

Source0:	https://github.com/PintaProject/Pinta/releases/download/%{version}/%{name}-%{version}.tar.gz

Requires:	hicolor-icon-theme
Requires:	mono-addins
Requires: mono
Requires: gtk-sharp2
Requires: glib-sharp2
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gtk-sharp2
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	mono-addins-devel
BuildRequires:	glib-sharp2
BuildRequires:  glib-gettextize

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}
  
%post
update-desktop-database &> /dev/null ||:

touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :

if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc readme.md license-mit.txt license-pdn.txt
%{_libdir}/%{name}
%{_libdir}/pkgconfig/pinta.pc
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/man/man1/%{name}*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/appdata/pinta.appdata.xml
%{_datadir}/metainfo/pinta.appdata.xml
