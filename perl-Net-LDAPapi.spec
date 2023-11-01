%undefine _debugsource_packages

%define module Net-LDAPapi
%define modparent Net
%define modname LDAPapi

Summary:	Perl bindings for LDAP client library
Name:		perl-%{module}
Version:	3.0.7
Release:	2
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/%{module}/
Source0:	https://cpan.metacpan.org/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	pkgconfig(ldap)
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	pkgconfig(libsasl2)

%description
Perl bindings for LDAP client library

%prep
%autosetup -p1 -n %{module}-%{version}

%build
#find -name \*.pm | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor -sdk 1 -lib_path %{_libdir} -include_path %{_includedir} -sasl_include_path %{_includedir} OPTIMIZE="%{optflags} -DLDAP_DEPRECATED"
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
