from timeit import default_timer
from IPython.display import clear_output

class progresstracker():
    def __init__(self, total_loops):
        self.total_loops = total_loops
        self.start_time = default_timer()
        self.loop_cnt = 0
        
    def __del__(self):
        del self.start_time
        del self.loop_cnt
    
    def reset(self, total_loops):
        self.total_loops = total_loops
        self.start_time = default_timer()
        self.loop_cnt = 0
        
    def step(self):
        """Perform step"""
        self.loop_cnt +=1
        progress = round(self.loop_cnt/self.total_loops * 100,1)
        
        current_time = default_timer()
        current_run_time = current_time - self.start_time
        expected_time = (current_run_time) / (self.loop_cnt/self.total_loops)
        expected_rest_time = expected_time - current_run_time
        
        return (progress, current_run_time, expected_time, expected_rest_time)
    
    def _calc_times(self,secs):
        hours = int(secs // 3600)
        secs = secs % 3600
        minutes = int(secs // 60)
        seconds = int(secs % 60)
        return seconds, minutes, hours
        
    def step_print(self, prefix="", suffix=""):
        """Perform step and print progess and times"""
        (progress, current_run_time, expected_time, expected_rest_time) = self.step()
        clear_output(True)
        if prefix != "":
            print(prefix)
        print("Current progress: {:3.1f} %".format(progress) )
        print("#" * int(progress*0.3))
        seconds, minutes, hours = self._calc_times(current_run_time)
        print("Current run time: {:02d}:{:02d}:{:02d}".format(hours,minutes,seconds))
        seconds, minutes, hours = self._calc_times(expected_rest_time)
        print("Expected time to finish: {:02d}:{:02d}:{:02d}".format(hours,minutes,seconds))
        if suffix != "":
            print(suffix)
        
        
if __name__ == "__main__":
    from time import sleep
    prog = progresstracker(100)
    for i in range(100):
        prog.step_print()
        sleep(1)
        
