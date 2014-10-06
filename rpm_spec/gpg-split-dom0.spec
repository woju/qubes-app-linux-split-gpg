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

Name:		qubes-gpg-split-dom0
Version:	%{version}
Release:	1%{dist}
Summary:    Qubes policy for gpg split

Group:		Qubes
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://www.qubes-os.org

Requires:	gpg

%define _builddir %(pwd)

%description

%prep
# we operate on the current directory, so no need to unpack anything

%build

%install
rm -rf $RPM_BUILD_ROOT
install -D qubes.Gpg.policy $RPM_BUILD_ROOT/etc/qubes-rpc/policy/qubes.Gpg
install -D qubes.GpgImportKey.policy $RPM_BUILD_ROOT/etc/qubes-rpc/policy/qubes.GpgImportKey
install -D qubes.GpgListKeys.policy $RPM_BUILD_ROOT/etc/qubes-rpc/policy/qubes.GpgListKeys
install -D qubes.GpgListSecretKeys.policy $RPM_BUILD_ROOT/etc/qubes-rpc/policy/qubes.GpgListSecretKeys

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config(noreplace) %attr(0664,root,qubes) /etc/qubes-rpc/policy/qubes.Gpg
%config(noreplace) %attr(0664,root,qubes) /etc/qubes-rpc/policy/qubes.GpgImportKey
%config(noreplace) %attr(0664,root,qubes) /etc/qubes-rpc/policy/qubes.GpgListKeys
%config(noreplace) %attr(0664,root,qubes) /etc/qubes-rpc/policy/qubes.GpgListSecretKeys
