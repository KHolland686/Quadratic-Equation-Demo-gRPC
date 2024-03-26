import grpc
import quadraticEquation_pb2
import quadraticEquation_pb2_grpc

def run():
    #Set a, b and c here. Easy to change as needed (add user input?)
    a = 2.0
    b = 3.0
    c = -2.0
    # print the coefficients being used to terminal
    print(f'\nSolving a Quadratic Equation with the values: a: {a}, b: {b}, c: {c}')
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = quadraticEquation_pb2_grpc.Quadratic_SolutionStub(channel)
        ## Generates a request internally with given coefficients
        response = stub.Solve_Quadratic_Equation(quadraticEquation_pb2.Quadratic_Request(a = a, b = b, c = c))
        # Generates solution
    print(f"Solution: {response.solution}")

if __name__ == '__main__':
    run()