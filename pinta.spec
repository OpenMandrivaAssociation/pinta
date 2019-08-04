%global debug_package %{nil}

Name:	    pinta
Version:	1.6
Release:	1
Summary:	An easy to use drawing and image editing program

Group:		Graphics

# the code is licensed under the MIT license while the icons are licensed as CC-BY
License:	MIT and CC-BY
URL:		http://pinta-project.com/

Source0:	http://github.com/downloads/PintaProject/Pinta/%{name}-%{version}.tar.gz

Requires:	hicolor-icon-theme
Requires:	mono-addins
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gtk-sharp2
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	mono-addins-devel
BuildRequires:	glib-sharp2

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup -q

chmod -x readme.md
chmod -x license-mit.txt
chmod -x license-pdn.txt
chmod -x xdg/pinta.1
chmod -x xdg/pinta.xpm
chmod -x xdg/scalable/pinta.svg

sed -i 's/\r//' readme.md
sed -i 's/\r//' license-mit.txt
sed -i 's/\r//' license-pdn.txt
sed -i 's/\r//' pinta.in
sed -i 's/\r//' xdg/pinta.xpm
sed -i 's/\r//' xdg/pinta.1
sed -i 's/\r//' xdg/scalable/pinta.svg

%build
%configure
%make

%install
%makeinstall_std

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

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
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/man/man1/%{name}*
%{_datadir}/pixmaps/%{name}*
