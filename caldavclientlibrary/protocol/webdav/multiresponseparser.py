##
# Copyright (c) 2007-2015 Apple Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

from caldavclientlibrary.protocol.webdav.xmlresponseparser import XMLResponseParser
from caldavclientlibrary.protocol.webdav.definitions import davxml

class MultiResponseParser(XMLResponseParser):

    def parse(self, multistatus_node):
        # Must have a node
        if multistatus_node is None:
            return

        # Verify that the node is the correct element <DAV:multistatus>
        if multistatus_node.tag != davxml.multistatus:
            return

        # Node is the right type, so iterator over all child response nodes and process each one
        for response in multistatus_node.getchildren():
            self.parseResponse(response)


    def parseResponse(self, response):
        raise NotImplementedError
