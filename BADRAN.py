# -*- coding: utf-8 -*-
geo.run_script(u'')
geo.global_registration(0, 100, 5000, False, 20, True, True, False)
geo.merge_point_grid_objects(u'Combined Points 1', True, False, True, False)
geo.select_disconnected_components(0, 5)
geo.delete()
geo.select_outliers(85)
geo.delete()
geo.compute_wrap(1, 0, 1, 4, 0, 0, 1, 2500000, 4, 0, 0, 0)
