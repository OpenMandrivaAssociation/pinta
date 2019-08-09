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
#Requires:	mono-addins
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gtk-sharp2
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
#BuildRequires:	mono-addins-devel
BuildRequires:	glib-sharp2

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup -q

# update the project and solution files for mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . \( -name "*.csproj" -o -name "*.proj" \) -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g; s#Mono.Posix, Version.*"#Mono.Posix"#g' {} \;

%build
%configure2_5x
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc readme.md license-mit.txt license-pdn.txt
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/man/man1/%{name}*
%{_datadir}/pixmaps/%{name}*
