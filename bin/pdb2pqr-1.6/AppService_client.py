##################################################
# file: AppService_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     ../ZSI-2.1-a1/scripts/wsdl2py wsdl/opal.wsdl
# 
##################################################

from .AppService_types import *
import urlparse
import types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD


# Locator
class AppServiceLocator:
    AppServicePort_address = "http://ws.nbcr.net:8080/axis/services/AppServicePort"

    @staticmethod
    def getAppServicePortAddress():
        return AppServiceLocator.AppServicePort_address

    @staticmethod
    def getAppServicePort(url=None, **kw):
        return AppServicePortTypeSoapBindingSOAP(url or AppServiceLocator.AppServicePort_address, **kw)


# Methods
class AppServicePortTypeSoapBindingSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: getAppMetadata
    def getAppMetadata(self, request, **kw):
        if isinstance(request, getAppMetadataRequest) is False:
            raise TypeError("%s incorrect request type" % request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://nbcr.sdsc.edu/opal/getAppMetadata", **kw)
        # no output wsaction
        response = self.binding.Receive(getAppMetadataResponse.typecode)
        return response

    # op: getAppConfig
    def getAppConfig(self, request, **kw):
        if isinstance(request, getAppConfigRequest) is False:
            raise TypeError("%s incorrect request type" % request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://nbcr.sdsc.edu/opal/getAppConfig", **kw)
        # no output wsaction
        response = self.binding.Receive(getAppConfigResponse.typecode)
        return response

    # op: launchJob
    def launchJob(self, request, **kw):
        if isinstance(request, launchJobRequest) is False:
            raise TypeError("%s incorrect request type" % request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://nbcr.sdsc.edu/opal/launchJob", **kw)
        # no output wsaction
        response = self.binding.Receive(launchJobResponse.typecode)
        return response

    # op: launchJobBlocking
    def launchJobBlocking(self, request, **kw):
        if isinstance(request, launchJobBlockingRequest) is False:
            raise TypeError("%s incorrect request type" % request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://nbcr.sdsc.edu/opal/launchJobBlocking", **kw)
        # no output wsaction
        response = self.binding.Receive(launchJobBlockingResponse.typecode)
        return response

    # op: queryStatus
    def queryStatus(self, request, **kw):
        if isinstance(request, queryStatusRequest) is False:
            raise TypeError("%s incorrect request type" % request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://nbcr.sdsc.edu/opal/queryStatus", **kw)
        # no output wsaction
        response = self.binding.Receive(queryStatusResponse.typecode)
        return response

    # op: getOutputs
    def getOutputs(self, request, **kw):
        if isinstance(request, getOutputsRequest) is False:
            raise TypeError("%s incorrect request type" % request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://nbcr.sdsc.edu/opal/getOutputs", **kw)
        # no output wsaction
        response = self.binding.Receive(getOutputsResponse.typecode)
        return response

    # op: getOutputAsBase64ByName
    def getOutputAsBase64ByName(self, request, **kw):
        if isinstance(request, getOutputAsBase64ByNameRequest) is False:
            raise TypeError("%s incorrect request type" % request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://nbcr.sdsc.edu/opal/getOutputAsBase64ByName", **kw)
        # no output wsaction
        response = self.binding.Receive(getOutputAsBase64ByNameResponse.typecode)
        return getOutputAsBase64ByNameResponse(response)

    # op: destroy
    def destroy(self, request, **kw):
        if isinstance(request, destroyRequest) is False:
            raise TypeError("%s incorrect request type" % request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://nbcr.sdsc.edu/opal/destroy", **kw)
        # no output wsaction
        response = self.binding.Receive(destroyResponse.typecode)
        return response


getAppMetadataRequest = GED("http://nbcr.sdsc.edu/opal/types", "getAppMetadataInput").pyclass

getAppMetadataResponse = GED("http://nbcr.sdsc.edu/opal/types", "getAppMetadataOutput").pyclass

getAppConfigRequest = GED("http://nbcr.sdsc.edu/opal/types", "getAppConfigInput").pyclass

getAppConfigResponse = GED("http://nbcr.sdsc.edu/opal/types", "getAppConfigOutput").pyclass

launchJobRequest = GED("http://nbcr.sdsc.edu/opal/types", "launchJobInput").pyclass

launchJobResponse = GED("http://nbcr.sdsc.edu/opal/types", "launchJobOutput").pyclass

launchJobBlockingRequest = GED("http://nbcr.sdsc.edu/opal/types", "launchJobBlockingInput").pyclass

launchJobBlockingResponse = GED("http://nbcr.sdsc.edu/opal/types", "launchJobBlockingOutput").pyclass

queryStatusRequest = GED("http://nbcr.sdsc.edu/opal/types", "queryStatusInput").pyclass

queryStatusResponse = GED("http://nbcr.sdsc.edu/opal/types", "queryStatusOutput").pyclass

getOutputsRequest = GED("http://nbcr.sdsc.edu/opal/types", "getOutputsInput").pyclass

getOutputsResponse = GED("http://nbcr.sdsc.edu/opal/types", "getOutputsOutput").pyclass

getOutputAsBase64ByNameRequest = GED("http://nbcr.sdsc.edu/opal/types", "getOutputAsBase64ByNameInput").pyclass

getOutputAsBase64ByNameResponse = GED("http://nbcr.sdsc.edu/opal/types", "getOutputAsBase64ByNameOutput").pyclass

destroyRequest = GED("http://nbcr.sdsc.edu/opal/types", "destroyInput").pyclass

destroyResponse = GED("http://nbcr.sdsc.edu/opal/types", "destroyOutput").pyclass
