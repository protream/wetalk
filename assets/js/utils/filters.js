import moment from 'moment'

moment.locale('zh-cn');

export function fromNow(time) {
  return moment(time).fromNow()
}