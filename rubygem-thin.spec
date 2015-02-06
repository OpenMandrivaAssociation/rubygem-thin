# Generated from thin-1.3.1.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	thin

Summary:	A thin and fast web server
Name:		rubygem-%{rbname}

Version:	1.3.1
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://code.macournoyer.com/thin/
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
Patch0:		thin-1.3.1-format-string-fixes.patch
BuildRequires:	rubygems 
BuildRequires:	ruby-devel

%description
A thin and fast web server

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .str_fmt~

%build
%gem_build

%install
%gem_install

%files
%{_bindir}/thin
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rack
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rack/adapter
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/backends
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/controllers
%dir %{ruby_sitearchdir}
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/backends/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/controllers/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/controllers/*.erb
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/%{rbname}
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rack/adapter/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/thin/*.erb
%{ruby_sitearchdir}/thin_parser.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3.1-2
+ Revision: 774531
- format string fixes (P0)
- drop build dependency on rake as it's now provided by ruby's standard library
- mass rebuild of ruby packages against ruby 1.9.1

* Tue Jan 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.3.1-1
+ Revision: 768092
- imported package rubygem-thin

