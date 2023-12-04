import argparse
import subprocess

def run_paraview():

    #Change this path to where the paraview executable is located
    subprocess.run("./Downloads/paraview/bin/paraview", shell=True)

def run_ogs():
    try:
        #Change to the necessary command to run ogs
        command = "singularity exec /home/liam/Downloads/Latest_sif/gcc_latest.sif ./Downloads/ogsbuild/bin/ogs -l debug Downloads/ISR/ISR/injection1.prj"
        completed_process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print OGS output
        print(completed_process.stdout)
        
        # If there are any errors, print them
        if completed_process.stderr:
            print(completed_process.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running OGS: {e}")
        # You can add further error handling here if needed.


def main():
    parser = argparse.ArgumentParser(description="Automate ParaView and OGS")
    parser.add_argument('--tool', choices=['paraview', 'ogs'], help="Choose the tool to run (paraview or ogs)")

    args = parser.parse_args()

    if args.tool == 'paraview':
        print("Running ParaView...")
        run_paraview()
        print("Paraview has Finished")
    elif args.tool == 'ogs':
        print("Running OGS...")
        run_ogs()
        print("OGS has finished.")
        print("Running Paraview")
        run_paraview()
        print("Paraview has Finished")
if __name__ == "__main__":
    main()

