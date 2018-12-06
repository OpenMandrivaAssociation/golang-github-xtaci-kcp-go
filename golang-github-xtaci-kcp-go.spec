Name:           golang-github-xtaci-kcp-go
Summary:        Production-Grade Reliable-UDP Library for golang
Version:        4.3.1
Release:        2%{?dist}
License:        MIT

# https://github.com/xtaci/kcp-go
%global repo    kcp-go
%global goipath github.com/xtaci/%{repo}
%global tag     v%{version}

%gometa

URL:            %{gourl}
Source0:        %{gourl}/archive/%{tag}/%{repo}-%{version}.tar.gz

# Add a patch to disable a failing test.
# It tries to open more than 1024 sockets, which doesn't work on fedora.
# See https://github.com/xtaci/kcp-go/issues/40
Patch0:         00-disable-failing-test.patch

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/klauspost/reedsolomon)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/templexxx/xor)
BuildRequires:  golang(github.com/tjfoc/gmsm/sm4)
BuildRequires:  golang(golang.org/x/crypto/blowfish)
BuildRequires:  golang(golang.org/x/crypto/cast5)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(golang.org/x/crypto/salsa20)
BuildRequires:  golang(golang.org/x/crypto/tea)
BuildRequires:  golang(golang.org/x/crypto/twofish)
BuildRequires:  golang(golang.org/x/crypto/xtea)
BuildRequires:  golang(golang.org/x/net/ipv4)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%autosetup -n %{repo}-%{version} -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 17 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1-2
- Use standard GitHub SourceURL again for consistency between releases.

* Mon Oct 08 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1-1
- Update to version 4.3.1.

* Sun Sep 30 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3-1
- Update to version 4.3.

* Sun Sep 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.1-1
- Update to version 4.1.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0-1
- Update to version 4.0.
- Update to spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 3.24-1
- Update to version 3.24.

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 3.23-1
- Update to version 3.23.

* Wed Nov 29 2017 Fabio Valentini <decathorpe@gmail.com> - 3.22-1
- Update to version 3.22.

* Tue Nov 21 2017 Fabio Valentini <decathorpe@gmail.com> - 3.21-1
- Update to version 3.21.

* Wed Nov 15 2017 Fabio Valentini <decathorpe@gmail.com> - 3.20-1
- Update to version 3.20.

* Thu Sep 14 2017 Fabio Valentini <decathorpe@gmail.com> - 3.19-2
- Add missing dependency breaking builds.

* Tue Sep 05 2017 Fabio Valentini <decathorpe@gmail.com> - 3.19-1
- Update to version 3.19.

* Tue Aug 01 2017 Fabio Valentini <decathorpe@gmail.com> - 3.18-1
- Update to version 3.18.

* Sun Jul 30 2017 Fabio Valentini <decathorpe@gmail.com> - 3.17-3
- Temporarily skip tests to fix dependency issues due to Mass Rebuild.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Fabio Valentini <decathorpe@gmail.com> - 3.17-1
- Update to version 3.17.

* Fri May 26 2017 Fabio Valentini <decathorpe@gmail.com> - 3.16-1
- Update to version 3.16.

* Wed May 17 2017 Fabio Valentini <decathorpe@gmail.com> - 3.15-1.20170517.git2fd1e3d
- Bump to commit 2fd1e3d (2017-05-17).

* Fri Mar 31 2017 Fabio Valentini <decathorpe@gmail.com> - 3.15-1
- First package for Fedora

