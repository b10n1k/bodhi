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

from cornice import Service

import bodhi.util
import bodhi.security


markdown = Service(name='markdowner', path='/markdown',
                   description='Markdown service',
                   cors_origins=bodhi.security.cors_origins_ro)


@markdown.get(accept=('application/json', 'text/json'), renderer='json')
@markdown.get(accept=('application/javascript'), renderer='jsonp')
def markdowner(request):
    """ Given some text, return the markdownified html version.

    We use this for "previews" of comments and update notes.
    """
    text = request.params.get('text')
    return dict(html=bodhi.util.markup(request.context, text))
