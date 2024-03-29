###
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC
###

moduleName = 'seedtime'

window.taigaContribPlugins = [] if !window.taigaContribPlugins

window.taigaContribPlugins.push({
    name: 'Seedtime',
    slug: 'seedtime',
    module: moduleName,
    authenticated: true,
})

angular.module(moduleName, [])
