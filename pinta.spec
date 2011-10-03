%global debug_package %{nil}

Name:		pinta
Version:	1.0
Release:	%mkrel 1
Summary:	An easy to use drawing and image editing program

Group:		Graphics

# the code is licensed under the MIT license while the icons are licensed as CC-BY
License:	MIT and CC-BY
URL:		http://pinta-project.com/

Source0:	http://github.com/downloads/jpobst/Pinta/%{name}-%{version}.tar.gz
      
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Mono only available on these:
ExclusiveArch: %ix86 x86_64 ppc ppc64 ia64 %{arm} sparcv9 alpha s390x

Requires:	hicolor-icon-theme
BuildRequires:	mono-devel, gtk-sharp2-devel, gettext, desktop-file-utils, glib-sharp2

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup -q

chmod -x readme.txt
chmod -x license-mit.txt
chmod -x license-pdn.txt
chmod -x todo.txt
chmod -x xdg/pinta.1
chmod -x xdg/pinta.desktop
chmod -x xdg/pinta.xpm
chmod -x xdg/scalable/pinta.svg

sed -i 's/\r//' readme.txt
sed -i 's/\r//' license-mit.txt
sed -i 's/\r//' license-pdn.txt
sed -i 's/\r//' todo.txt
sed -i 's/\r//' pinta.in
sed -i 's/\r//' xdg/pinta.desktop
sed -i 's/\r//' xdg/pinta.xpm
sed -i 's/\r//' xdg/pinta.1
sed -i 's/\r//' xdg/scalable/pinta.svg

sed -i -e 's!$(InstallPrefix)/lib/!$(InstallPrefix)/%{_lib}/!' Pinta/Pinta.csproj
sed -i -e 's!@prefix@/lib/!%{_libdir}/!' pinta.in
sed -i -i 's!$(InstallPrefix)/lib/!$(InstallPrefix)/%{_lib}/!' Pinta.Install.proj

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %name
  
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

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc todo.txt readme.txt license-mit.txt license-pdn.txt
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/man/man1/%{name}*
%{_datadir}/pixmaps/%{name}*
