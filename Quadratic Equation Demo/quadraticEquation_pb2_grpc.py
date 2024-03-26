# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import quadraticEquation_pb2 as quadraticEquation__pb2


class Quadratic_SolutionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Solve_Quadratic_Equation = channel.unary_unary(
                '/Quadratic_Solution/Solve_Quadratic_Equation',
                request_serializer=quadraticEquation__pb2.Quadratic_Request.SerializeToString,
                response_deserializer=quadraticEquation__pb2.Quadratic_Response.FromString,
                )


class Quadratic_SolutionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Solve_Quadratic_Equation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Quadratic_SolutionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Solve_Quadratic_Equation': grpc.unary_unary_rpc_method_handler(
                    servicer.Solve_Quadratic_Equation,
                    request_deserializer=quadraticEquation__pb2.Quadratic_Request.FromString,
                    response_serializer=quadraticEquation__pb2.Quadratic_Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Quadratic_Solution', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Quadratic_Solution(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Solve_Quadratic_Equation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Quadratic_Solution/Solve_Quadratic_Equation',
            quadraticEquation__pb2.Quadratic_Request.SerializeToString,
            quadraticEquation__pb2.Quadratic_Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
