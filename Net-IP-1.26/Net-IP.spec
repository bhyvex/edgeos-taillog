
Summary: Net::IP Perl module
Name: perl-Net-IP
Version: 1.26
Release: 1
Source0: Net-IP-%{version}.tar.gz
License: Perl
Group: Development/Languages
BuildRoot: %{_tmppath}/%{name}-root

%description
IP - Perl extension for manipulating IPv4/IPv6 addresses

%prep
%setup -q -n Net-IP-%{version}
%{__perl} Makefile.PL INSTALLSCRIPT=%{_prefix}/bin
%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/lib/perl5/site_perl/*/Net
%{_prefix}/lib/perl5/man/man3/*
%{_prefix}/bin


