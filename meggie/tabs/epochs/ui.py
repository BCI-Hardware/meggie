"""
"""
import logging

from pprint import pformat

from meggie.tabs.epochs.dialogs.createEpochsFromEventsDialogMain import CreateEpochsFromEventsDialog


def epochs_info(experiment, data, window):
    """ Fills info element
    """
    try:
        selected_name = data['outputs']['epochs'][0]
        epochs = experiment.active_subject.epochs[selected_name]
        params = epochs.params

        filtered = {key: params[key] for key in
                    ['bstart', 'bend', 'tmin', 'tmax', 'events']}
        message = pformat(filtered)
    except BaseException:
        message = ""

    return message


def create_from_events(experiment, data, window):
    """ Opens epoch creation dialog
    """
    dialog = CreateEpochsFromEventsDialog(experiment, window)
    dialog.show()


def delete(experiment, data, window):
    """ Deletes selected epochs item from active subject
    """
    subject = experiment.active_subject
    try:
        selected_name = data['outputs']['epochs'][0]
    except IndexError as exc:
        return

    subject.remove(selected_name, 'epochs')
    experiment.save_experiment_settings()
    window.initialize_ui()


def delete_from_all(experiment, data, window):
    """ Deletes selected epochs item from all subjects
    """
    try:
        selected_name = data['outputs']['epochs'][0]
    except IndexError as exc:
        return

    for subject in experiment.subjects.values():
        if selected_name in subject.epochs:
            try:
                subject.remove(selected_name, 'epochs')
            except Exception as exc:
                logging.getLogger('ui_logger').warning(
                    'Could not remove epochs for ' +
                    subject.name)
    experiment.save_experiment_settings()
    window.initialize_ui()


def plot_epochs(experiment, data, window):
    """ Plots selected item
    """
    subject = experiment.active_subject
    try:
        selected_name = data['outputs']['epochs'][0]
    except IndexError as exc:
        return

    epochs = subject.epochs.get(selected_name)
    epochs.content.plot()


def plot_image(experiment, data, window):
    """ Plots selected item using plot_image
    """
    subject = experiment.active_subject
    try:
        selected_name = data['outputs']['epochs'][0]
    except IndexError as exc:
        return

    epochs = subject.epochs.get(selected_name)
    epochs.content.plot_image()
