#
# This is the SPEC file for creating binary and source RPMs for the VMs.
#
#
# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2011  Marek Marczykowski <marmarek@invisiblethingslab.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#

%{!?version: %define version %(cat version)}

Name:		qubes-gpg-split
Version:	%{version}
Release:	1%{dist}
Summary:	The Qubes service for secure gpg separation

Group:		Qubes
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://www.qubes-os.org

Requires:	gpg

%define _builddir %(pwd)

%description
The Qubes service for delegating gpg actions to other VM. You can keep keys in
secure (even network isolated) VM and only pass data to it for
signing/decryption.

%prep
# we operate on the current directory, so no need to unpack anything

%build
make clean
make build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/qubes-gpg-split
install -t $RPM_BUILD_ROOT/usr/lib/qubes-gpg-split src/pipe-cat src/gpg-server
install -D src/gpg-client $RPM_BUILD_ROOT/usr/bin/qubes-gpg-client
install -D gpg-client-wrapper $RPM_BUILD_ROOT/usr/bin/qubes-gpg-client-wrapper
install -D gpg-import-key $RPM_BUILD_ROOT/usr/bin/qubes-gpg-import-key
install -D qubes.Gpg.service $RPM_BUILD_ROOT/etc/qubes-rpc/qubes.Gpg
install -D qubes.GpgImportKey.service $RPM_BUILD_ROOT/etc/qubes-rpc/qubes.GpgImportKey
install -D qubes.GpgListKeys.service $RPM_BUILD_ROOT/etc/qubes-rpc/qubes.GpgListKeys
install -D qubes.GpgListSecretKeys.service $RPM_BUILD_ROOT/etc/qubes-rpc/qubes.GpgListSecretKeys
install -D qubes-gpg.sh $RPM_BUILD_ROOT/etc/profile.d/qubes-gpg.sh
install -d $RPM_BUILD_ROOT/var/run/qubes-gpg-split
install -D qubes-gpg-split.tmpfiles $RPM_BUILD_ROOT/etc/tmpfiles.d/qubes-gpg-split.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir /usr/lib/qubes-gpg-split
/usr/lib/qubes-gpg-split/gpg-server
/usr/lib/qubes-gpg-split/pipe-cat
/usr/bin/qubes-gpg-client
/usr/bin/qubes-gpg-client-wrapper
/usr/bin/qubes-gpg-import-key
%attr(0644,root,root) /etc/qubes-rpc/qubes.Gpg
%attr(0644,root,root) /etc/qubes-rpc/qubes.GpgImportKey
%attr(0644,root,root) /etc/qubes-rpc/qubes.GpgListKeys
%attr(0644,root,root) /etc/qubes-rpc/qubes.GpgListSecretKeys
/etc/profile.d/qubes-gpg.sh
%dir %attr(0777,root,root) /var/run/qubes-gpg-split
/etc/tmpfiles.d/qubes-gpg-split.conf
