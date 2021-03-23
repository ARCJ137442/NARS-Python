"""
    Author: Christian Hahm
    Created: December 24, 2020
"""
import tkinter as tk


class Global:
    """
        NARS vars
    """
    NARS = None  # variable to hold NARS instance
    current_cycle_number = 0  # total number of working cycles executed so far
    paused = False
    ID_MARKER = "ID:"
    ID_END_MARKER = ": "


class GlobalGUI:
    """
        GUI vars and functions
    """
    # Interface vars
    gui_output_textbox = None  # primary output gui
    gui_delay_slider = None  # delay slider
    gui_total_cycles_lbl = None
    play_pause_button = None

    # Internal Data vars
    gui_experience_buffer_listbox = None  # output for tasks in experience buffer
    gui_concept_bag_listbox = None  # output for concepts in memory bag
    gui_buffer_output_label = None
    gui_concepts_output_label = None
    GUI_PRIORITY_SYMBOL = "$"

    # booleans
    gui_use_internal_data = False
    gui_use_interface = False

    @classmethod
    def print_to_output(cls, msg, data_structure=None):
        """
            Print a message to an output GUI box

            Should only called by output thread
        """

        listbox = None
        if data_structure is Global.NARS.overall_experience_buffer:
            listbox = GlobalGUI.gui_experience_buffer_listbox
        elif data_structure is Global.NARS.memory.concepts_bag:
            listbox = GlobalGUI.gui_concept_bag_listbox
        elif data_structure is None:  # interface output
            if cls.gui_use_interface:
                cls.gui_output_textbox.insert(tk.END, msg + "\n")
            else:
                print(msg)

        if listbox is None: return

        # internal data output
        # insert item sorted by priority
        if GlobalGUI.gui_use_internal_data:
            string_list = listbox.get(0, tk.END)  # get all items in the listbox
            msg_priority = msg[msg.find(GlobalGUI.GUI_PRIORITY_SYMBOL) + 1:msg.rfind(GlobalGUI.GUI_PRIORITY_SYMBOL)]
            idx_to_insert = tk.END  # by default insert at the end
            i = 0
            for row in string_list:
                row_priority = row[row.find(GlobalGUI.GUI_PRIORITY_SYMBOL) + 1:row.rfind(GlobalGUI.GUI_PRIORITY_SYMBOL)]
                if float(msg_priority) >= float(row_priority):
                    idx_to_insert = i
                    break
                i = i + 1
            listbox.insert(idx_to_insert, msg)
            if data_structure is Global.NARS.overall_experience_buffer:
                GlobalGUI.gui_buffer_output_label.config(text="Task Buffer: " + str(len(data_structure)))
            elif data_structure is Global.NARS.memory.concepts_bag:
                GlobalGUI.gui_concepts_output_label.config(text="Concepts: " + str(len(data_structure)))

    @classmethod
    def remove_from_output(cls, msg, data_structure=None):
        """
            Remove a message from an output GUI box

            Should only be called by output thread
        """
        if Global.NARS is None: return
        if data_structure is Global.NARS.overall_experience_buffer:
            listbox = GlobalGUI.gui_experience_buffer_listbox
        elif data_structure is Global.NARS.memory.concepts_bag:
            listbox = GlobalGUI.gui_concept_bag_listbox

        if GlobalGUI.gui_use_internal_data:
            string_list = listbox.get(0, tk.END)
            msg_id = msg[len(Global.ID_MARKER):msg.rfind(Global.ID_END_MARKER)]  # assuming ID is at the beginning, get characters from ID: to first spacebar
            idx_to_remove = -1
            i = 0
            for row in string_list:
                row_id = row[len(Global.ID_MARKER):row.rfind(Global.ID_END_MARKER)]
                if msg_id == row_id:
                    idx_to_remove = i
                    break
                i = i + 1
            if idx_to_remove == -1:
                assert False, "GUI Error: cannot find msg to remove: " + msg
            listbox.delete(idx_to_remove)

            if data_structure is Global.NARS.overall_experience_buffer:
                GlobalGUI.gui_buffer_output_label.config(text="Task Buffer: " + str(len(data_structure)))
            elif data_structure is Global.NARS.memory.concepts_bag:
                GlobalGUI.gui_concepts_output_label.config(text="Concepts: " + str(len(data_structure)))

    @classmethod
    def set_paused(cls, paused):
        """
            Sets the Global paused parameter and changes the GUI button
        """
        Global.paused = paused
        if Global.paused:
            GlobalGUI.play_pause_button.config(text="PLAY")
        else:
            GlobalGUI.play_pause_button.config(text="PAUSE")
