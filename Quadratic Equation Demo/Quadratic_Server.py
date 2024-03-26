import grpc
import math
import quadraticEquation_pb2
import quadraticEquation_pb2_grpc
import concurrent.futures

class quadratic_Equation_Solver(quadraticEquation_pb2_grpc.Quadratic_SolutionServicer):
    '''
    Method to solve the quadratic equation. Takes the three coefficients a, b, c sent from client and solves for x (two possible answers)
    '''
    def Solve_Quadratic_Equation(self,request,context):
        a = request.a
        b = request.b
        c = request.c

        root = b**2 - 4 * a * c
        # If the discriminant/root is negative, return response stating solutions are imaginary
        if root < 0:
            return quadraticEquation_pb2.QuadraticResponse(
                solution = "The dicriminant is negative, so the solutions are complex or imaginary"
            )
        else:
            # Otherwise, solve for x1 and x2 
            x1 = (-b + math.sqrt(root)) / (2 * a)
            x2 = (-b - math.sqrt(root)) / (2 * a)
            return quadraticEquation_pb2.Quadratic_Response(solution = f"The two solutions for x are {x1} or {x2}")
        
def serve():
    port = "50051"
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers = 10))
    quadraticEquation_pb2_grpc.add_Quadratic_SolutionServicer_to_server(quadratic_Equation_Solver(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
