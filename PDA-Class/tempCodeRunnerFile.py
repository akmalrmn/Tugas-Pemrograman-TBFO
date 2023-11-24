    html_path = input("Enter the HTML file path: ")
        self.start_input, line_count = HTMLToString(html_path)
        print("Checking word \"" + self.start_input + "\" ...")

        while self.start_input != "end":
            # magic starts here
            if not self.generate(self.start_state, self.start_input, self.bottom_stack,
                                    [(self.start_state, self.start_input, self.bottom_stack)]):
                print(f"Syntax error at line {line_count}")  # Display line number where syntax error occurred
                self.finish()
            else:
                self.print_config(self.accepted_config)  # show a list of configurations for acceptance
                self.finish()

            file_path = input("Enter the HTML file path: ")
            self.start_input, line_count = HTMLToString(file_path)
            print("Checking word \"