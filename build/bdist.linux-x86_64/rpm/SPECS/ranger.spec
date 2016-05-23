%define name ranger
%define version 1.7.2
%define unmangled_version 1.7.2
%define release 1

Summary: Vim-like file manager
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPL3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Roman Zimbelmann <hut@hut.pm>
Url: http://ranger.nongnu.org

%description
A console file manager with VI key bindings.

It provides a minimalistic and nice curses interface with a view on the
directory hierarchy.  The secondary task of ranger is to figure out which
program you want to use to open your files with.


%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
