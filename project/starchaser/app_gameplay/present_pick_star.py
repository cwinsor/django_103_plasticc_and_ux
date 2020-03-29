import logging
import pandas as pd


# a class representing the results from Plasticc
class PresentPickStar():

    def __init__(self, qs_starlist, df_btrotta, df_kboone):

        # convert QuerySet to DataFrame on the way in...
        self._df_starlist = pd.DataFrame.from_records(qs_starlist.values())
        self._df_btrotta = df_btrotta
        self._df_kboone = df_kboone

        self._star_hdr    = self._df_starlist.columns
        self._btrotta_hdr = self._df_btrotta.columns
        self._kboone_hdr  = self._df_kboone.columns

        logger = logging.getLogger(__name__)
        logger.debug("\n---df_star  \n" + str(self._df_starlist))
        logger.debug("\n---df_btrott\n" + str(self._df_btrotta))
        logger.debug("\n---df_kboone\n" + str(self._df_kboone))

        #logger.debug("\n---here7\n" + str(self._star_hdr))
        #logger.debug("\n---here8\n" + str(len(present_pick_star.star_hdr())))

        merge_result_1 = self._df_starlist.merge(
            right = self._df_btrotta,
            how = 'outer',
            left_on = 'star_id',
            right_on = 'a',
            suffixes=('_s', '_x')
        )

        logger.debug("\n---merge_result_1\n" + str(merge_result_1))

        merge_result_2 = merge_result_1.merge(
            right = self._df_kboone,
            how = 'outer',
            left_on = 'star_id',
            right_on = 'a',
            suffixes=('_x', '_y')
        )
        logger.debug("\n---merge_result_2\n" + str(merge_result_2))

        self._row_data = []
        #for x in merge_result_2.iterrows():
        for x in merge_result_2.itertuples():
            logger.debug("\n---type" + str(type(x)))
            logger.debug("\n---vals" + str(x))
            #logger.debug("\n---..." + str(x.star_id) + " " + str(x.ra))
            self._row_data.append(x)

        logger.debug("\n---row_data\n" + str(self._row_data))


        #row1 = {'star_values': [1, 2, 3], 'btrotta_values': [4, 5, 6], 'kboone_values': [0,1,2]}
        #row2 = {'star_values': [0, 2, 3], 'btrotta_values': [4, 5, 6], 'kboone_values': [0,1,2]}
        #self._row_data = [row1, row2]


    def star_hdr(self):
        return self._star_hdr

    def btrotta_hdr(self):
        return self._btrotta_hdr

    def kboone_hdr(self):
        return self._kboone_hdr

    def star_hdr_len(self):
        return len(self._star_hdr)

    def btrotta_hdr_len(self):
        return len(self._btrotta_hdr)

    def kboone_hdr_len(self):
        return len(self._kboone_hdr)
    
    def rows(self):
        return self._row_data



