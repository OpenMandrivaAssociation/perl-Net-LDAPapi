%define module Net-LDAPapi
%define modparent Net
%define modname LDAPapi

Summary:	Perl bindings for LDAP client library
Name:		perl-%{module}
Version:	3.0.3
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	openldap-devel
BuildRequires:	glibc-devel
%if %{?mdkversion:1}%{?!mdkversion:0}
BuildRequires:	perl-devel >= 5.8.0
%endif
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Perl bindings for LDAP client library

%prep

%setup -q -n %{module}-%{version}

%build
#find -name \*.pm | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor -sdk 1 -lib_path %{_libdir} -include_path %{_includedir}
%make

%check
#make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Credits Changes examples
%{perl_vendorarch}/%{modparent}/*.pm
%{perl_vendorarch}/auto/%{modparent}/%{modname}
%{_mandir}/*/*
