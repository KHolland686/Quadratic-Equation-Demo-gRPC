import grpc
import quadraticEquation_pb2
import quadraticEquation_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = quadraticEquation_pb2_grpc.solve_Quadratic_Equation_Stub(channel)
        ## Generates a request fromm proto file and passes it to the 'solver' in server.
        response = stub.Solve_Quadratic_Equation(quadraticEquation_pb2.quadratic_Request(a = 2.0, b = 3.0, c = -2.0))
        # CHANGE a, b, c to solve for different equations! (or add user input?)
    print(f"Solution: {response.solution}")

if __name__ == '__main__':
    run()