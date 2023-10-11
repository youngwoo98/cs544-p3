# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import modelserver_pb2 as modelserver__pb2


class ModelServerStub(object):
    """services (RPC functions)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetCoefs = channel.unary_unary(
                '/ModelServer/SetCoefs',
                request_serializer=modelserver__pb2.SetCoefsRequest.SerializeToString,
                response_deserializer=modelserver__pb2.SetCoefsResp.FromString,
                )
        self.Predict = channel.unary_unary(
                '/ModelServer/Predict',
                request_serializer=modelserver__pb2.PredictRequest.SerializeToString,
                response_deserializer=modelserver__pb2.PredictResp.FromString,
                )


class ModelServerServicer(object):
    """services (RPC functions)
    """

    def SetCoefs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetCoefs': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCoefs,
                    request_deserializer=modelserver__pb2.SetCoefsRequest.FromString,
                    response_serializer=modelserver__pb2.SetCoefsResp.SerializeToString,
            ),
            'Predict': grpc.unary_unary_rpc_method_handler(
                    servicer.Predict,
                    request_deserializer=modelserver__pb2.PredictRequest.FromString,
                    response_serializer=modelserver__pb2.PredictResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ModelServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModelServer(object):
    """services (RPC functions)
    """

    @staticmethod
    def SetCoefs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ModelServer/SetCoefs',
            modelserver__pb2.SetCoefsRequest.SerializeToString,
            modelserver__pb2.SetCoefsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ModelServer/Predict',
            modelserver__pb2.PredictRequest.SerializeToString,
            modelserver__pb2.PredictResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
