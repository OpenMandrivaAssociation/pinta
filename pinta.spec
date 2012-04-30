%global debug_package %{nil}

Name:		pinta
Version:	1.3
Release:	%mkrel 1
Summary:	An easy to use drawing and image editing program

Group:		Graphics

# the code is licensed under the MIT license while the icons are licensed as CC-BY
License:	MIT and CC-BY
URL:		http://pinta-project.com/

Source0:	%{name}-%{version}.tar.gz
      
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Mono only available on these:
ExclusiveArch: %ix86 x86_64 ppc ppc64 ia64 %{arm} sparcv9 alpha s390x

Requires:	hicolor-icon-theme
Requires:	desktop-file-utils
Requires:	mono(gdk-sharp) 
Requires:	mono(glib-sharp)
Requires:	mono(gtk-sharp)
Requires:	mono(ICSharpCode.SharpZipLib) 
Requires:	mono(Mono.Addins) 
Requires:	mono(Mono.Addins.Gui)
Requires:	mono(Mono.Cairo)
Requires:	mono(Mono.Posix)
Requires:	mono(mscorlib) 
Requires:	mono(pango-sharp)
Requires:	mono(System) 
Requires:	mono(System.Core) 
Requires:	mono(System.Xml) 
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gtk-sharp2
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	glib-sharp2
BuildRequires:	mono-addins-devel 

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup -q

%build
%configure2_5x
make

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
%doc todo.txt license-mit.txt license-pdn.txt
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/man/man1/%{name}*
%{_datadir}/pixmaps/*
