%undefine _debugsource_packages

%define module Net-LDAPapi
%define modparent Net
%define modname LDAPapi

Summary:	Perl bindings for LDAP client library
Name:		perl-%{module}
Version:	3.0.7
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	openldap-devel
BuildRequires:	glibc-devel
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	pkgconfig(libsasl2)

%description
Perl bindings for LDAP client library

%prep
%autosetup -p1 -n %{module}-%{version}

%build
#find -name \*.pm | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor -sdk 1 -lib_path %{_libdir} -include_path %{_includedir} -sasl_include_path %{_includedir}
%make_build

%if 0
%check
make test
%endif

%install
%make_install

%files
%defattr(-,root,root)
%doc Credits Changes examples
%{perl_vendorarch}/%{modparent}/*.pm
%{perl_vendorarch}/auto/%{modparent}/%{modname}
%{_mandir}/*/*
