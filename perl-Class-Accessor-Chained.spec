#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Accessor-Chained
Version  : 0.01
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Class-Accessor-Chained-0.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Class-Accessor-Chained-0.01.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Class-Accessor-Chained-man
Requires: perl(Class::Accessor)
BuildRequires : perl(Class::Accessor)

%description
=head1 NAME
Class::Accessor::Chained - make chained accessors
=head1 SYNOPSIS
package Foo;
use base qw( Class::Accessor::Chained );
__PACKAGE__->mk_accessors(qw( foo bar baz ));

%package man
Summary: man components for the perl-Class-Accessor-Chained package.
Group: Default

%description man
man components for the perl-Class-Accessor-Chained package.


%prep
%setup -q -n Class-Accessor-Chained-0.01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Class/Accessor/Chained.pm
/usr/lib/perl5/site_perl/5.26.1/Class/Accessor/Chained/Fast.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Accessor::Chained.3
/usr/share/man/man3/Class::Accessor::Chained::Fast.3
