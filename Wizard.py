from tkinter import Frame, Button


class Step(Frame):
    # parent is tkinter container, data is a dictionary where data will be stored, stepname is unique string and
    # is the key for data in the dictionary
    def __init__(self, parent, data, stepname):
        super().__init__(parent)
        self.parent = parent
        self.data = data
        self.stepname = stepname

        if stepname not in self.data:
            # initialize key/value in dictionary, creating nested dictionary
            self.data[stepname] = {}
        else:
            print(stepname + " appears to be a duplicate of a previous step!")

        self.completed = True
        self.previous_enabled = True

    # Wizard Steps should call this once it is ok to advance to the next step
    # Will result in the "Next" or "Finish" buttons becoming enabled/interactive/not grayed out
    def _step_completed(self):
        self.completed = True
        # send event up to parent container (which should be the wizard)
        self.parent.event_generate("<<step_complete>>", when="tail")

    # Wizard Steps should call this if the user does something to make the wizard block clicking next
    # For instance, if there was a valid email address and now there isn't
    def _step_not_completed(self):
        self.completed = False
        # send event up to parent container (which should be the wizard)
        self.parent.event_generate("<<step_not_complete>>", when="tail")


    # The Wizard calls this for the Step when it comes into view
    def onscreen_enter(self):
        pass

    # The Wizard calls this for the Step when it is removed from view
    def onscreen_exit(self):
        pass

    def allow_previous(self):
        return self.previous_enabled

    def allow_next(self):
        return self.completed


class Wizard(Frame):
    # parent is tkinter container, data is a dictionary where data will be stored for each Wizard step
    def __init__(self, parent, data):
        super().__init__(parent)

        self.parent = parent

        self.current_step = None
        self.current_step_index = 0

        self.steps = []
        self.data = data

        self.button_frame = Frame(self, bd=1, relief="raised")
        self.content_frame = Frame(self)

        self.back_button = Button(self.button_frame, text="<< Back", command=self.back)
        self.next_button = Button(self.button_frame, text="Next >>", command=self.next)
        self.finish_button = Button(self.button_frame, text="Finish", command=self.finish)

        # self.content_frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
        self.content_frame.pack(side="top", fill="both", expand=True)

        # self.button_frame.pack_propagate(0)
        self.button_frame.pack(side="bottom", fill="x")

        # register for events that steps might pass up to the wizard
        self.bind("<<step_complete>>", self.step_complete)
        self.bind("<<step_not_complete>>", self.step_not_complete)

        # Example custom event call for above bind()
        # self.event_generate("<<step_complete>>", when="tail")

    def step_complete(self, event):
        # print("Wizard:step_complete()")
        self.next_button.config(state="normal")
        self.finish_button.config(state="normal")

    def step_not_complete(self, event):
        # print("Wizard:step_complete()")
        self.next_button.config(state="disabled")
        self.finish_button.config(state="disabled")

    def set_steps(self, steps):
        self.steps = steps

    def start(self):
        self.show_step(self.current_step_index)

    def back(self):
        self.current_step_index -= 1
        self.show_step(self.current_step_index)

    def next(self):
        self.current_step_index += 1
        self.show_step(self.current_step_index)

    def finish(self):
        self.current_step_index = 0

        print("data is: ")
        print(self.data)

        self.parent.quit()

    def show_step(self, step):

        if step < len(self.steps):
            if self.current_step is not None:
                # remove current step and tell the step it is going off screen
                self.current_step.onscreen_exit()
                self.current_step.pack_forget()

            self.current_step = self.steps[step]
            self.current_step.pack(fill="both", expand=True)

            # Tell the step it's going up on the screen
            self.current_step.onscreen_enter()

        if len(self.steps) != 0:
            if len(self.steps) == 1:
                self.back_button.pack_forget()
                self.next_button.pack_forget()
                self.finish_button.pack(side="right")
            elif step == 0:
                # first step
                self.back_button.pack_forget()
                self.next_button.pack(side="right")
                self.finish_button.pack_forget()

            elif step == len(self.steps)-1:
                # last step
                self.back_button.pack(side="left")
                self.next_button.pack_forget()
                self.finish_button.pack(side="right")

            else:
                # all other steps
                self.back_button.pack(side="left")
                self.next_button.pack(side="right")
                self.finish_button.pack_forget()
        else:
            self.back_button.pack_forget()
            self.next_button.pack_forget()
            self.finish_button.pack(side="right")

        if self.current_step is not None:
            if self.current_step.allow_next():
                self.next_button.config(state="normal")
                self.finish_button.config(state="normal")
            else:
                self.next_button.config(state="disabled")
                self.finish_button.config(state="disabled")

            if not self.current_step.allow_previous():
                self.back_button.pack_forget()


if __name__ == "__main__":

    from tkinter import Tk, Label, Button, Frame

    # A wizard step for testing purposes
    class TestingDemoStep(Step):

        def button0_clicked(self):
            print("button0_clicked")

            # The following demonstrates how to tell the wizard that a step has been satisfied
            # For instance, the user cannot advance until they have entered some information
            self._step_completed()

        def button1_clicked(self):
            print("button1_clicked")

            # The following demonstrates how to tell the wizard that a step has been satisfied
            # For instance, the user cannot advance until they have entered some information
            self._step_not_completed()

        def onscreen_enter(self):
            super().onscreen_enter()

            print("Step: " + self.stepname + " is now on the screen!")

        def onscreen_exit(self):
            super().onscreen_exit()

            print("Step: " + self.stepname + " is now leaving the screen!")

        def __init__(self, parent, data, stepname, iscomplete=True, isprevenabled=True):
            super().__init__(parent, data, stepname)

            self.completed = iscomplete
            self.previous_enabled = isprevenabled
            header = Label(self, text="This is a wizard step #: " + " " + self.stepname, bd=2, relief="groove")
            header.pack(side="top", fill="x")

            btn0 = Button(self, text="Click Me!", command=self.button0_clicked)
            btn0.pack(side="top", fill="x")

            btn1 = Button(self, text="Undo complete", command=self.button1_clicked)
            btn1.pack(side="top", fill="x")

            self.data[self.stepname]["demo"] = "DEMO STEP"


    root = Tk()

    data = {}
    my_gui = Wizard(root, data)
    steps = [TestingDemoStep(my_gui, data, "one", False, False),
             TestingDemoStep(my_gui, data, "two", True, False),
             TestingDemoStep(my_gui, data, "three", False, True)]

    my_gui.set_steps(steps)
    my_gui.pack()
    my_gui.start()

    root.mainloop()
