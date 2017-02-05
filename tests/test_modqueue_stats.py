"""Hal9000 responder modqueue stats test"""

from hal9000.plugins.modqueue_stats import modqueue_stats


def test_modqueue_stats(mocker):
    log_mock = mocker.patch('hal9000.plugins.modqueue_stats.logger')
    reddit_mock = mocker.patch('hal9000.plugins.modqueue_stats.reddit')

    comment_mock = mocker.Mock()
    comment_mock.name = 't1_comment'
    submission_mock = mocker.Mock()
    submission_mock.name = 't3_submission'
    modqueue = [comment_mock, comment_mock, submission_mock]

    reddit_mock.subreddit.return_value.mod.modqueue.return_value = modqueue

    message = mocker.Mock()

    modqueue_stats(message)

    call_args = str(message.reply.call_args)
    assert '3 items' in call_args
    assert '2 comments' in call_args
    assert '1 submissions' in call_args
    assert '1 pages' in call_args


def test_modqueue_stats_empty(mocker):
    log_mock = mocker.patch('hal9000.plugins.modqueue_stats.logger')
    reddit_mock = mocker.patch('hal9000.plugins.modqueue_stats.reddit')
    message = mocker.Mock()
    sr_mock = mocker.Mock()
    sr_mock.mod.modqueue.return_value = []
    reddit_mock.subreddit.return_value = sr_mock

    modqueue_stats(message)

    call_args = str(message.reply.call_args)
    assert 'empty' in call_args

