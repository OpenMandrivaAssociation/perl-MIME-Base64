%define upstream_name    MIME-Base64
%define upstream_version 3.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 3.14
Release:    1

Summary:    Encode/decode Base 64 (RFC 2045)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MIME/MIME-Base64-3.14.tar.gz


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




%changelog
* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.130.0-2mdv2012.0
+ Revision: 763376
- rebuild

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.130.0-1mdv2011.0
+ Revision: 601901
- update to new version 3.13

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.100.0-1mdv2011.0
+ Revision: 597104
- update to 3.10

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 3.90.0-3mdv2011.0
+ Revision: 562430
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 3.90.0-2mdv2011.0
+ Revision: 556005
- rebuild for perl 5.12

* Wed Jan 27 2010 Jérôme Quelin <jquelin@mandriva.org> 3.90.0-1mdv2010.1
+ Revision: 496997
- update to 3.09

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 3.80.0-1mdv2010.0
+ Revision: 395246
- import perl-MIME-Base64


* Sun Jul 12 2009 cpan2dist 3.08-1mdv
- initial mdv release, generated with cpan2dist

