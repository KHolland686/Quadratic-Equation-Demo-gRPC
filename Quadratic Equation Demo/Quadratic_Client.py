import grpc
import quadraticEquation_pb2
import quadraticEquation_pb2_grpc

def run():
    #Takes uer input for coefficients
    a = float(input("Enter the coefficient for 'a': "))
    b = float(input("Enter the coefficient for 'b': "))
    c = float(input("Enter the coefficient for 'c': "))
    sign_b = '-' if b < 0 else '+'
    sign_c = '-' if c < 0 else '+'
    # print the coefficients being used to terminal
    print(f'\nSolving a Quadratic Equation with the values: a: {a}, b: {b}, c: {c} \n Or : {a}x² {sign_b} {abs(b)}x {sign_c} {abs(c)} = 0')
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = quadraticEquation_pb2_grpc.Quadratic_SolutionStub(channel)
        ## Generates a request internally with given coefficients
        response = stub.Solve_Quadratic_Equation(quadraticEquation_pb2.Quadratic_Request(a = a, b = b, c = c))
        # Generates solution
    print(f"Solution: {response.solution}")

if __name__ == '__main__':
    run()