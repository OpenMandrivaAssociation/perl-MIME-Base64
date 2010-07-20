%define upstream_name    MIME-Base64
%define upstream_version 3.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Encode/decode Base 64 (RFC 2045)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz


BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides functions to encode and decode strings into and from
the base64 encoding specified in RFC 2045 - _MIME (Multipurpose Internet
Mail Extensions)_. The base64 encoding is designed to represent arbitrary
sequences of octets in a form that need not be humanly readable. A
65-character subset ([A-Za-z0-9+/=]) of US-ASCII is used, enabling 6 bits
to be represented per printable character.

The following functions are provided:

* encode_base64($str)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


