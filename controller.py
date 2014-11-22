import model
import view
import sys
from datetime import datetime

class Game:
    def __init__ (self):
        if view.welcome():
            self.login(view.login())
        else:
            self.sign_up(view.sign_up())

    def sign_up(self, obj):
        db = model.DB()
        this_user = db.create_user(obj['name'], obj['password'])
        if this_user:
            self.next_round(this_user)
        else:
            self.sign_up( view.name_exists() )

    def login(self, obj):
        db = model.DB()
        verify = db.fetch_user(obj['name'], obj['password'])
        if verify:
            self.next_round(verify)
        else:
            view.incorrect_password()

    def new_round(self, last_turn = None):
        new_turn = Turn.create_turn()
        now_turn.start_time = datetime.now()
        rpn_as_string = ''.join(new_turn.rpn.equation)
        info_obj = {}
        info_obj.rpn = rpn_as_string
        if last_turn:
            info_obj.time_taken = (last_turn.end_time - last_turn.start_time)
            info_obj.last_rpn = last_turn.rpn.equation
            info_obj.answer = last_turn.rpn.answer_equation
            info_obj.right_or_wrong = last_turn.correct_incorrect
        answer = view.show_rpn(info_obj)
        new_turn.correct_incorrect = (new_turn.rpn.answer_equation == answer)
        new_turn.end_time = datetime.now()
        new_turn.time_taken = new_turn.end_time - new_turn.start_time
        db.save_turn(new_turn)
        self.new_round(new_turn)

    def check_high_scores(self):
        #get high scores from model/db
        #pass scores to view
        pass

    def check_personal_stats(self):
        #get personal stats from model/db
        #pass scores to view
        pass

    def end_game(self):
        model.close_db()
        sys.exit()

this_game = Game()
